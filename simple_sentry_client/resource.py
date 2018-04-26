from simple_rest_client.resource import Resource

from . import actions


class Issues(Resource):
    actions = actions.issues_actions


class ProjectIssues(Resource):
    actions = actions.projects_issues_actions


class ProjectEvents(Resource):
    actions = actions.projects_events_actions


class Organizations(Resource):
    actions = actions.organizations_actions


class Projects(Resource):
    actions = actions.projects_actions


class ProjectsDsyms(Resource):
    actions = actions.projects_dsyms_actions


class ProjectsDsymsUpload(Resource):
    actions = actions.projects_dsyms_upload_actions


class ProjectsHooks(Resource):
    actions = actions.projects_hooks_actions


class ProjectsKeys(Resource):
    actions = actions.projects_keys_actions


class ProjectsUserFeedback(Resource):
    actions = actions.projects_user_feedback_actions


class OrganizationsReleases(Resource):
    actions = actions.organizations_releases_actions


class OrganizationsReleasesDeploys(Resource):
    actions = actions.organizations_releases_deploys_actions


class OrganizationsReleasesFileUpload(Resource):
    actions = actions.organizations_releases_file_upload_actions


class OrganizationsReleasesFiles(Resource):
    actions = actions.organizations_releases_files_actions


class ProjectsReleases(Resource):
    actions = actions.projects_releases_actions


class ProjectsReleasesFileUpload(Resource):
    actions = actions.projects_releases_file_upload_actions


class ProjectsReleasesFiles(Resource):
    actions = actions.projects_releases_files_actions


class OrganizationsTeams(Resource):
    actions = actions.organizations_teams_actions


class Teams(Resource):
    actions = actions.teams_actions


class TeamsProjects(Resource):
    actions = actions.teams_projects_actions
