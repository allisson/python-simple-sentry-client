from simple_rest_client.resource import AsyncResource

from . import actions


class Issues(AsyncResource):
    actions = actions.issues_actions


class ProjectIssues(AsyncResource):
    actions = actions.projects_issues_actions


class ProjectEvents(AsyncResource):
    actions = actions.projects_events_actions


class Organizations(AsyncResource):
    actions = actions.organizations_actions


class Projects(AsyncResource):
    actions = actions.projects_actions


class ProjectsDsyms(AsyncResource):
    actions = actions.projects_dsyms_actions


class ProjectsHooks(AsyncResource):
    actions = actions.projects_hooks_actions


class ProjectsKeys(AsyncResource):
    actions = actions.projects_keys_actions


class ProjectsUserFeedback(AsyncResource):
    actions = actions.projects_user_feedback_actions


class OrganizationsReleases(AsyncResource):
    actions = actions.organizations_releases_actions


class OrganizationsReleasesDeploys(AsyncResource):
    actions = actions.organizations_releases_deploys_actions


class OrganizationsReleasesFileUpload(AsyncResource):
    actions = actions.organizations_releases_file_upload_actions


class OrganizationsReleasesFiles(AsyncResource):
    actions = actions.organizations_releases_files_actions


class ProjectsReleases(AsyncResource):
    actions = actions.projects_releases_actions


class ProjectsReleasesFileUpload(AsyncResource):
    actions = actions.projects_releases_file_upload_actions


class ProjectsReleasesFiles(AsyncResource):
    actions = actions.projects_releases_files_actions


class OrganizationsTeams(AsyncResource):
    actions = actions.organizations_teams_actions


class Teams(AsyncResource):
    actions = actions.teams_actions


class TeamsProjects(AsyncResource):
    actions = actions.teams_projects_actions
