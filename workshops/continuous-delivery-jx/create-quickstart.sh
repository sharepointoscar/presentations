# create a quickstart project
# since my github org is free, repo must be public.
jx create quickstart --git-public

jx create quickstart --language javascript --project-name carsweb --batch-mode


# get app activities
jx get activities -f carsweb

# get build logs, pick app pipeline
jx get build logs