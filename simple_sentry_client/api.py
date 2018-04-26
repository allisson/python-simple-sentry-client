from simple_rest_client.api import API

from . import resource
from . import async_resource


def get_api_instance(token='', api_root_url=None, timeout=3, resource_class=resource):
    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/json'
    }
    file_upload_headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'multipart/form-data'
    }
    api_root_url = api_root_url or 'https://sentry.io/api/0/'
    api = API(api_root_url=api_root_url, headers=headers, json_encode_body=True, timeout=timeout)
    api.add_resource(resource_name='issues', resource_class=getattr(resource_class, 'Issues'))
    api.add_resource(resource_name='project_issues', resource_class=getattr(resource_class, 'ProjectIssues'))
    api.add_resource(resource_name='project_events', resource_class=getattr(resource_class, 'ProjectEvents'))
    api.add_resource(resource_name='organizations', resource_class=getattr(resource_class, 'Organizations'))

    api.add_resource(resource_name='projects', resource_class=getattr(resource_class, 'Projects'))
    api.add_resource(resource_name='projects_dsyms', resource_class=getattr(resource_class, 'ProjectsDsyms'))
    api.add_resource(
        resource_name='projects_dsyms_upload', resource_class=getattr(resource_class, 'ProjectsDsymsUpload'),
        json_encode_body=False, headers=file_upload_headers
    )
    api.add_resource(resource_name='projects_hooks', resource_class=getattr(resource_class, 'ProjectsHooks'))
    api.add_resource(resource_name='projects_keys', resource_class=getattr(resource_class, 'ProjectsKeys'))
    api.add_resource(
        resource_name='projects_user_feedback', resource_class=getattr(resource_class, 'ProjectsUserFeedback')
    )
    api.add_resource(
        resource_name='organizations_releases',
        resource_class=getattr(resource_class, 'OrganizationsReleases')
    )
    api.add_resource(
        resource_name='organizations_releases_deploys',
        resource_class=getattr(resource_class, 'OrganizationsReleasesDeploys')
    )
    api.add_resource(
        resource_name='organizations_releases_file_upload',
        resource_class=getattr(resource_class, 'OrganizationsReleasesFileUpload'), json_encode_body=False,
        headers=file_upload_headers
    )
    api.add_resource(
        resource_name='organizations_releases_files',
        resource_class=getattr(resource_class, 'OrganizationsReleasesFiles')
    )
    api.add_resource(
        resource_name='projects_releases',
        resource_class=getattr(resource_class, 'ProjectsReleases')
    )
    api.add_resource(
        resource_name='projects_releases_file_upload',
        resource_class=getattr(resource_class, 'ProjectsReleasesFileUpload'), json_encode_body=False,
        headers=file_upload_headers
    )
    api.add_resource(
        resource_name='projects_releases_files',
        resource_class=getattr(resource_class, 'ProjectsReleasesFiles')
    )
    api.add_resource(
        resource_name='organizations_teams',
        resource_class=getattr(resource_class, 'OrganizationsTeams')
    )
    api.add_resource(resource_name='teams', resource_class=getattr(resource_class, 'Teams'))
    api.add_resource(resource_name='teams_projects', resource_class=getattr(resource_class, 'TeamsProjects'))
    return api


def get_async_api_instance(token='', api_root_url=None, timeout=3):
    return get_api_instance(
        token=token, api_root_url=api_root_url, timeout=timeout, resource_class=async_resource
    )
