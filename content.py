import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/home/strongestavenger/Bitbucket/web_application_final")
# Your mock repo
mock_repo = git.Repo("/home/strongestavenger/Github/merge-workflows")
importer = Importer([repo], mock_repo)
# Use a list of emails if more than one
importer.set_author(['michaelmukalo@gmail.com', 'mikemutoro@gmail.com'])
print("rscwx")
