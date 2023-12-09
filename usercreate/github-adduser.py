from github import Github
from github import Team
from github import NamedUser

access_token = "Your Personal Access Token"

g = Github(access_token)

org = g.get_organization("Your Organisation name")
org.login

# Invite user using email and role
org.invite_user(
    email='email of the invitee',
    role='direct_member')
# Other possible roles are: ["admin", "direct_member", "billing_manager"