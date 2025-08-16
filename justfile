set shell := ["cmd.exe", "/c"]

serve_doc:
    uv run mkdocs serve

publish_doc:
    uv run mkdocs build
    uv run mkdocs gh-deploy

publish_package:
    uv build
    uv publish