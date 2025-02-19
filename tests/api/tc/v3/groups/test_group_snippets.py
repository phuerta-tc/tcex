"""Test the TcEx API Snippets."""
# standard-library
# standard library
import base64
import time

# first-party
from tcex.api.tc.v3.tql.tql_operator import TqlOperator
from tests.api.tc.v3.v3_helpers import TestV3, V3Helper


class TestGroupSnippets(TestV3):
    """Test TcEx API Interface."""

    example_pdf = None
    v3 = None

    def setup_method(self):
        """Configure setup before all tests."""
        print('')  # ensure any following print statements will be on new line
        self.v3_helper = V3Helper('groups')
        self.v3 = self.v3_helper.v3
        self.tcex = self.v3_helper.tcex

        self.example_pdf = (
            r'JVBERi0xLjIgCjkgMCBvYmoKPDwKPj4Kc3RyZWFtCkJULyAzMiBUZiggIFRjRXggVGVzdGluZyAg'
            r'ICknIEVUCmVuZHN0cmVhbQplbmRvYmoKNCAwIG9iago8PAovVHlwZSAvUGFnZQovUGFyZW50IDUg'
            r'MCBSCi9Db250ZW50cyA5IDAgUgo+PgplbmRvYmoKNSAwIG9iago8PAovS2lkcyBbNCAwIFIgXQov'
            r'Q291bnQgMQovVHlwZSAvUGFnZXMKL01lZGlhQm94IFsgMCAwIDI1MCA1MCBdCj4+CmVuZG9iagoz'
            r'IDAgb2JqCjw8Ci9QYWdlcyA1IDAgUgovVHlwZSAvQ2F0YWxvZwo+PgplbmRvYmoKdHJhaWxlcgo8'
            r'PAovUm9vdCAzIDAgUgo+PgolJUVPRgo='
        )

        # remove old cases
        groups = self.tcex.v3.groups()
        groups.filter.summary(TqlOperator.EQ, 'MyAdversary')
        for group in groups:
            group.delete()

    #
    # Create Group
    #

    def test_group_create(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )

        group.create(params={'owner': 'TCI'})
        # End Snippet

        # Add cleanup
        group.delete()

    def test_group_stage_group_associations(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )

        # Add association
        association = self.tcex.v3.group(name='MyThreat', type='Threat')
        group.stage_associated_group(association)

        group.create(params={'owner': 'TCI'})
        # End Snippet

        # Add cleanup
        group.delete()

    def test_group_stage_indicator_associations(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )

        # Add association
        association = self.tcex.v3.indicator(ip='111.111.111.111', type='Address')
        group.stage_associated_indicator(association)

        group.create(params={'owner': 'TCI'})
        # End Snippet

        # Add cleanup
        group.delete()

    def test_group_stage_attribute(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )

        # Add attribute
        attribute = self.tcex.v3.group_attribute(
            value='An example description attribute.',
            type='Description',
        )
        group.stage_attribute(attribute)

        group.create(params={'owner': 'TCI'})
        # End Snippet

        # Add cleanup
        group.delete()

    def test_group_stage_security_label(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )

        # stage security label
        security_label = self.tcex.v3.security_label(name='TLP:WHITE')
        group.stage_security_label(security_label)

        group.create(params={'owner': 'TCI'})
        # End Snippet

        # Add cleanup
        group.delete()

    def test_group_stage_tag(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )

        # stage tag
        tag = self.tcex.v3.tag(name='Example-Tag')
        group.stage_tag(tag)

        group.create(params={'owner': 'TCI'})
        # End Snippet

        # Add cleanup
        group.delete()

    #
    # Delete / Remove
    #

    def test_group_delete_by_id(self):
        """Test snippet"""
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )
        group.create(params={'owner': 'TCI'})

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)
        group.delete(params={'owner': 'TCI'})
        # End Snippet

    def test_group_delete_attribute(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
            attributes=[
                {
                    'type': 'Description',
                    'value': 'An example description attribute',
                },
                {
                    'type': 'Description',
                    'value': 'Another example description attribute',
                },
            ],
        )
        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)
        for attribute in group.attributes:
            if attribute.model.value == 'An example description attribute':
                attribute.delete()
        # End Snippet

    def test_group_remove_group_associations(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
            associated_groups=[
                {'name': 'MyGroup0', 'type': 'Adversary'},
                {'name': 'MyGroup', 'type': 'Adversary'},
            ],
        )

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)

        for association in group.associated_groups:
            if association.model.name == 'MyGroup':
                # IMPORTANT the "remove()" method will remove the association from the group and
                #    the "delete()" method will remove the association from the system.
                association.remove()
        # End Snippet

    def test_group_remove_indicator_associations(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
            associated_indicators=[
                {'ip': '111.111.111.111', 'type': 'Address'},
                {'ip': '222.222.222.222', 'type': 'Address'},
            ],
        )

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)

        for association in group.associated_indicators:
            if association.model.summary == '222.222.222.222':
                # IMPORTANT: the "remove()" method will remove the association from the group and
                #    the "delete()" method will remove the indicator from the system.
                association.remove()
        # End Snippet

    def test_group_remove_security_label(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
            security_labels=[
                {'name': 'TLP:WHITE'},
                {'name': 'TLP:GREEN'},
            ],
        )

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)

        for security_label in group.security_labels:
            if security_label.model.name == 'TLP:WHITE':
                # IMPORTANT the "remove()" method will remove the security label from the group and
                #    the "delete()" method will remove the security label from the system.
                security_label.remove()
        # End Snippet

    def test_group_remove_tag(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
            tags={'name': 'Example-Tag'},
        )

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)

        for tag in group.tags:
            if tag.model.name == 'Example-Tag':
                # IMPORTANT the "remove()" method will remove the tag from the group and
                #    the "delete()" method will remove the tag from the system.
                tag.remove()
        # End Snippet

    def test_group_remove_tag_using_mode(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
            tags={'name': 'Example-Tag'},
        )

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)
        updated_group = self.tcex.v3.group(id=group.model.id)
        for tag in group.tags:
            if tag.model.name == 'Example-Tag':
                # IMPORTANT the "remove()" method will remove the tag from the group and
                #    the "delete()" method will remove the tag from the system.
                updated_group.stage_tag(tag)
        updated_group.update()
        # End Snippet

    #
    # Get Group
    #

    def test_group_get_by_id(self):
        """Test snippet"""
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )
        group.create(params={'owner': 'TCI'})

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id, params={'fields': ['_all_']})
        group.get()
        # End Snippet

    def test_group_get_tql(self):
        """Test snippet"""
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )
        group.create(params={'owner': 'TCI'})

        # Begin Snippet
        groups = self.tcex.v3.groups()
        groups.filter.date_added(TqlOperator.GT, '1 day ago')
        groups.filter.id(TqlOperator.EQ, group.model.id)
        groups.filter.owner_name(TqlOperator.EQ, 'TCI')
        groups.filter.type_name(TqlOperator.EQ, 'Adversary')
        for group in groups:
            print(group.model.dict(exclude_none=True))
        # End Snippet

    #
    # Update
    #

    def test_group_update(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            name='MyAdversary',
            type='Adversary',
        )

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)
        # This will update the confidence to "50"
        group.model.name = 50
        group.update(params={'owner': 'TCI'})
        # End Snippet

    #
    # Download / Upload
    #

    def test_document_download_pdf(self):
        """Test snippet"""
        # Begin Snippet
        group = self.tcex.v3.group(
            name='MyAdversary',
            type='Adversary',
        )
        group.create(params={'owner': 'TCI'})

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)
        _ = group.pdf()  # pdf is returned as bytes
        # End Snippet

    def test_document_upload(self):
        """Test snippet"""
        file_content = base64.b64decode(self.example_pdf)
        # Begin Snippet
        group = self.tcex.v3.group(
            file_name='example.pdf',
            name='MyDocument',
            type='Document',
        )
        group.create(params={'owner': 'TCI'})
        response = group.upload(file_content)
        if not response.ok:
            print(f'The upload failed: {response.reason}')
        # End Snippet

        group.delete()

    def test_document_download(self):
        """Test snippet"""
        group = self.v3_helper.create_group(
            file_name='example.pdf',
            name='MyDocument',
            type_='Document',
        )
        file_content = base64.b64decode(self.example_pdf)
        _ = group.upload(file_content)

        # provide it enough time to upload the file.
        time.sleep(1)

        # Begin Snippet
        group = self.tcex.v3.group(id=group.model.id)
        _ = group.download()  # content is returned as bytes
        if not group.request.ok:
            print(f'The download failed: {group.request.reason}')
        # End Snippet
