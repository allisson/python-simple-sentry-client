issues_actions = {
    'list': {
        'method': 'GET',
        'url': 'issues/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'issues/{}/',
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'issues/{}/',
    },
    'events': {
        'method': 'GET',
        'url': 'issues/{}/events/',
    },
    'events_latest': {
        'method': 'GET',
        'url': 'issues/{}/events/latest/',
    },
    'events_oldest': {
        'method': 'GET',
        'url': 'issues/{}/events/oldest/',
    },
    'hashes': {
        'method': 'GET',
        'url': 'issues/{}/hashes/',
    },
    'tags': {
        'method': 'GET',
        'url': 'issues/{}/tags/{}/',
    },
    'tags_values': {
        'method': 'GET',
        'url': 'issues/{}/tags/{}/values/',
    },
}
projects_issues_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/issues/'
    },
    'update': {
        'method': 'PUT',
        'url': 'projects/{}/{}/issues/',
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'projects/{}/{}/issues/',
    },
}
projects_events_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/events/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'projects/{}/{}/events/{}/'
    },
}
organizations_actions = {
    'list': {
        'method': 'GET',
        'url': 'organizations/'
    },
    'create': {
        'method': 'POST',
        'url': 'organizations/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'organizations/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'organizations/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'organizations/{}/'
    },
    'projects': {
        'method': 'GET',
        'url': 'organizations/{}/projects/'
    },
    'repos': {
        'method': 'GET',
        'url': 'organizations/{}/repos/'
    },
    'repos_commits': {
        'method': 'GET',
        'url': 'organizations/{}/repos/{}/commits/'
    },
    'shortids': {
        'method': 'GET',
        'url': 'organizations/{}/shortids/{}/'
    },
    'stats': {
        'method': 'GET',
        'url': 'organizations/{}/stats/'
    },
}
projects_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'projects/{}/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'projects/{}/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'projects/{}/{}/'
    },
    'stats': {
        'method': 'GET',
        'url': 'projects/{}/{}/stats/'
    },
    'users': {
        'method': 'GET',
        'url': 'projects/{}/{}/users/'
    },
    'tags_values': {
        'method': 'GET',
        'url': 'projects/{}/{}/tags/{}/values/'
    },
}
projects_dsyms_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/files/dsyms/'
    },
}
projects_dsyms_upload_actions = {
    'create': {
        'method': 'POST',
        'url': 'projects/{}/{}/files/dsyms/'
    },
}
projects_hooks_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/hooks/'
    },
    'create': {
        'method': 'POST',
        'url': 'projects/{}/{}/hooks/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'projects/{}/{}/hooks/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'projects/{}/{}/hooks/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'projects/{}/{}/hooks/{}/'
    },
}
projects_keys_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/keys/'
    },
    'create': {
        'method': 'POST',
        'url': 'projects/{}/{}/keys/'
    },
    'update': {
        'method': 'PUT',
        'url': 'projects/{}/{}/keys/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'projects/{}/{}/keys/{}/'
    },
}
projects_user_feedback_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/user-feedback/'
    },
    'create': {
        'method': 'POST',
        'url': 'projects/{}/{}/user-feedback/'
    },
}
organizations_releases_actions = {
    'list': {
        'method': 'GET',
        'url': 'organizations/{}/releases/'
    },
    'create': {
        'method': 'POST',
        'url': 'organizations/{}/releases/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'organizations/{}/releases/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'organizations/{}/releases/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'organizations/{}/releases/{}/'
    },
    'commitfiles': {
        'method': 'GET',
        'url': 'organizations/{}/releases/{}/commitfiles/'
    },
    'commits': {
        'method': 'GET',
        'url': 'organizations/{}/releases/{}/commits/'
    },
}
organizations_releases_deploys_actions = {
    'list': {
        'method': 'GET',
        'url': 'organizations/{}/releases/{}/deploys/'
    },
    'create': {
        'method': 'POST',
        'url': 'organizations/{}/releases/{}/deploys/'
    },
}
organizations_releases_file_upload_actions = {
    'create': {
        'method': 'POST',
        'url': 'organizations/{}/releases/{}/files/'
    },
}
organizations_releases_files_actions = {
    'list': {
        'method': 'GET',
        'url': 'organizations/{}/releases/{}/files/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'organizations/{}/releases/{}/files/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'organizations/{}/releases/{}/files/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'organizations/{}/releases/{}/files/{}/'
    },
}
projects_releases_actions = {
    'commits': {
        'method': 'GET',
        'url': 'projects/{}/{}/releases/{}/commits/'
    },
    'resolved': {
        'method': 'GET',
        'url': 'projects/{}/{}/releases/{}/resolved/'
    },
}
projects_releases_file_upload_actions = {
    'create': {
        'method': 'POST',
        'url': 'projects/{}/{}/releases/{}/files/'
    },
}
projects_releases_files_actions = {
    'list': {
        'method': 'GET',
        'url': 'projects/{}/{}/releases/{}/files/'
    },
    'retrieve': {
        'method': 'GET',
        'url': 'projects/{}/{}/releases/{}/files/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'projects/{}/{}/releases/{}/files/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'projects/{}/{}/releases/{}/files/{}/'
    },
}
organizations_teams_actions = {
    'list': {
        'method': 'GET',
        'url': 'organizations/{}/teams/'
    },
    'create': {
        'method': 'POST',
        'url': 'organizations/{}/teams/'
    },
}
teams_actions = {
    'retrieve': {
        'method': 'GET',
        'url': 'teams/{}/{}/'
    },
    'update': {
        'method': 'PUT',
        'url': 'teams/{}/{}/'
    },
    'destroy': {
        'method': 'DELETE',
        'url': 'teams/{}/{}/'
    },
    'stats': {
        'method': 'GET',
        'url': 'teams/{}/{}/stats/'
    },
}
teams_projects_actions = {
    'list': {
        'method': 'GET',
        'url': 'teams/{}/{}/projects/'
    },
    'create': {
        'method': 'POST',
        'url': 'teams/{}/{}/projects/'
    },
}
