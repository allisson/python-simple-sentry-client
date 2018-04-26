from simple_rest_client.resource import AsyncResource

from . import actions


class Issues(AsyncResource):
    actions = actions.issues_actions


class ProjectIssues(AsyncResource):
    actions = actions.project_issues_actions


class ProjectEvents(AsyncResource):
    actions = actions.project_events_actions


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


class OrganizationsReleasesFiles(AsyncResource):
    actions = actions.organizations_releases_files_actions
