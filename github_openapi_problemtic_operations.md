# Problematic Operations in GitHub API Spec

Found 46 problematic operations out of 1028

## Schema Example Mismatch: 25 operations

- Removed problematic operation: actions/re-run-job-for-workflow-run (POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun)
- Removed problematic operation: actions/re-run-workflow (POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun)
- Removed problematic operation: actions/re-run-workflow-failed-jobs (POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs)
- Removed problematic operation: actions/review-custom-gates-for-run (POST /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule)
- Removed problematic operation: checks/create (POST /repos/{owner}/{repo}/check-runs)
- Removed problematic operation: checks/update (PATCH /repos/{owner}/{repo}/check-runs/{check_run_id})
- Removed problematic operation: code-scanning/create-variant-analysis (POST /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses)
- Removed problematic operation: codespaces/create-for-authenticated-user (POST /user/codespaces)
- Removed problematic operation: issues/add-labels (POST /repos/{owner}/{repo}/issues/{issue_number}/labels)
- Removed problematic operation: issues/set-labels (PUT /repos/{owner}/{repo}/issues/{issue_number}/labels)
- Removed problematic operation: markdown/render-raw (POST /markdown/raw)
- Removed problematic operation: markdown/render-raw (POST /markdown/raw)
- Removed problematic operation: orgs/convert-member-to-outside-collaborator (PUT /orgs/{org}/outside_collaborators/{username})
- Removed problematic operation: projects/create-card (POST /projects/columns/{column_id}/cards)
- Removed problematic operation: pulls/request-reviewers (POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers)
- Removed problematic operation: repos/add-status-check-contexts (POST /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts)
- Removed problematic operation: repos/add-team-access-restrictions (POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams)
- Removed problematic operation: repos/create-pages-site (POST /repos/{owner}/{repo}/pages)
- Removed problematic operation: repos/remove-status-check-contexts (DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts)
- Removed problematic operation: repos/remove-team-access-restrictions (DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams)
- Removed problematic operation: repos/set-status-check-contexts (PUT /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts)
- Removed problematic operation: repos/set-team-access-restrictions (PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams)
- Removed problematic operation: repos/update-information-about-pages-site (PUT /repos/{owner}/{repo}/pages)
- Removed problematic operation: users/add-email-for-authenticated-user (POST /user/emails)
- Removed problematic operation: users/delete-email-for-authenticated-user (DELETE /user/emails)

## Request Body Schema Issue: 52 operations

- Removed problematic operation: actions/review-custom-gates-for-run (POST /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule)
- Removed problematic operation: apps/update-webhook-config-for-app (PATCH /app/hook/config)
- Removed problematic operation: checks/create (POST /repos/{owner}/{repo}/check-runs)
- Removed problematic operation: checks/update (PATCH /repos/{owner}/{repo}/check-runs/{check_run_id})
- Removed problematic operation: code-scanning/create-variant-analysis (POST /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses)
- Removed problematic operation: codespaces/create-for-authenticated-user (POST /user/codespaces)
- Removed problematic operation: codespaces/create-or-update-secret-for-authenticated-user (PUT /user/codespaces/secrets/{secret_name})
- Removed problematic operation: gists/create (POST /gists)
- Removed problematic operation: issues/add-labels (POST /repos/{owner}/{repo}/issues/{issue_number}/labels)
- Removed problematic operation: issues/create (POST /repos/{owner}/{repo}/issues)
- Removed problematic operation: issues/create (POST /repos/{owner}/{repo}/issues)
- Removed problematic operation: issues/create (POST /repos/{owner}/{repo}/issues)
- Removed problematic operation: issues/set-labels (PUT /repos/{owner}/{repo}/issues/{issue_number}/labels)
- Removed problematic operation: issues/update (PATCH /repos/{owner}/{repo}/issues/{issue_number})
- Removed problematic operation: issues/update (PATCH /repos/{owner}/{repo}/issues/{issue_number})
- Removed problematic operation: issues/update (PATCH /repos/{owner}/{repo}/issues/{issue_number})
- Removed problematic operation: orgs/create-or-update-custom-properties (PATCH /orgs/{org}/properties/schema)
- Removed problematic operation: orgs/create-or-update-custom-properties-values-for-repos (PATCH /orgs/{org}/properties/values)
- Removed problematic operation: orgs/create-or-update-custom-property (PUT /orgs/{org}/properties/schema/{custom_property_name})
- Removed problematic operation: orgs/create-webhook (POST /orgs/{org}/hooks)
- Removed problematic operation: orgs/update-webhook (PATCH /orgs/{org}/hooks/{hook_id})
- Removed problematic operation: orgs/update-webhook-config-for-org (PATCH /orgs/{org}/hooks/{hook_id}/config)
- Removed problematic operation: projects/create-card (POST /projects/columns/{column_id}/cards)
- Removed problematic operation: pulls/request-reviewers (POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers)
- Removed problematic operation: repos/add-status-check-contexts (POST /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts)
- Removed problematic operation: repos/add-team-access-restrictions (POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams)
- Removed problematic operation: repos/create-deployment (POST /repos/{owner}/{repo}/deployments)
- Removed problematic operation: repos/create-or-update-custom-properties-values (PATCH /repos/{owner}/{repo}/properties/values)
- Removed problematic operation: repos/create-org-ruleset (POST /orgs/{org}/rulesets)
- Removed problematic operation: repos/create-org-ruleset (POST /orgs/{org}/rulesets)
- Removed problematic operation: repos/create-org-ruleset (POST /orgs/{org}/rulesets)
- Removed problematic operation: repos/create-org-ruleset (POST /orgs/{org}/rulesets)
- Removed problematic operation: repos/create-org-ruleset (POST /orgs/{org}/rulesets)
- Removed problematic operation: repos/create-pages-site (POST /repos/{owner}/{repo}/pages)
- Removed problematic operation: repos/create-repo-ruleset (POST /repos/{owner}/{repo}/rulesets)
- Removed problematic operation: repos/create-webhook (POST /repos/{owner}/{repo}/hooks)
- Removed problematic operation: repos/remove-status-check-contexts (DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts)
- Removed problematic operation: repos/remove-team-access-restrictions (DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams)
- Removed problematic operation: repos/set-status-check-contexts (PUT /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts)
- Removed problematic operation: repos/set-team-access-restrictions (PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams)
- Removed problematic operation: repos/update-information-about-pages-site (PUT /repos/{owner}/{repo}/pages)
- Removed problematic operation: repos/update-information-about-pages-site (PUT /repos/{owner}/{repo}/pages)
- Removed problematic operation: repos/update-org-ruleset (PUT /orgs/{org}/rulesets/{ruleset_id})
- Removed problematic operation: repos/update-org-ruleset (PUT /orgs/{org}/rulesets/{ruleset_id})
- Removed problematic operation: repos/update-org-ruleset (PUT /orgs/{org}/rulesets/{ruleset_id})
- Removed problematic operation: repos/update-org-ruleset (PUT /orgs/{org}/rulesets/{ruleset_id})
- Removed problematic operation: repos/update-org-ruleset (PUT /orgs/{org}/rulesets/{ruleset_id})
- Removed problematic operation: repos/update-repo-ruleset (PUT /repos/{owner}/{repo}/rulesets/{ruleset_id})
- Removed problematic operation: repos/update-webhook (PATCH /repos/{owner}/{repo}/hooks/{hook_id})
- Removed problematic operation: repos/update-webhook-config-for-repo (PATCH /repos/{owner}/{repo}/hooks/{hook_id}/config)
- Removed problematic operation: users/add-email-for-authenticated-user (POST /user/emails)
- Removed problematic operation: users/delete-email-for-authenticated-user (DELETE /user/emails)

## Non Json Content: 2 operations

- Removed problematic operation: markdown/render-raw (POST /markdown/raw)
- Removed problematic operation: repos/upload-release-asset (POST /repos/{owner}/{repo}/releases/{release_id}/assets)

## Parameter Schema Issue: 2 operations

- Removed problematic operation: security-advisories/list-global-advisories (GET /advisories)
- Removed problematic operation: security-advisories/list-global-advisories (GET /advisories)

## Detailed Analysis

### Index 115: actions/re-run-job-for-workflow-run
Path: POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun

Issues detected:
- Schema-example mismatch in application/json: Schema type is object but example is not an object

### Index 116: actions/re-run-workflow
Path: POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun

Issues detected:
- Schema-example mismatch in application/json: Schema type is object but example is not an object

### Index 117: actions/re-run-workflow-failed-jobs
Path: POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs

Issues detected:
- Schema-example mismatch in application/json: Schema type is object but example is not an object

### Index 126: actions/review-custom-gates-for-run
Path: POST /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses anyOf schema (complex, 2 variants)

### Index 225: apps/update-webhook-config-for-app
Path: PATCH /app/hook/config

Issues detected:
- RequestBody schema issue in application/json: Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 239: checks/create
Path: POST /repos/{owner}/{repo}/check-runs

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 250: checks/update
Path: PATCH /repos/{owner}/{repo}/check-runs/{check_run_id}

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses anyOf schema (complex, 2 variants)

### Index 259: code-scanning/create-variant-analysis
Path: POST /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 3 variants)

### Index 304: codespaces/create-for-authenticated-user
Path: POST /user/codespaces

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 307: codespaces/create-or-update-secret-for-authenticated-user
Path: PUT /user/codespaces/secrets/{secret_name}

Issues detected:
- RequestBody schema issue in application/json: Property 'selected_repository_ids' - Array items - Uses anyOf schema (complex, 2 variants)

### Index 382: gists/create
Path: POST /gists

Issues detected:
- RequestBody schema issue in application/json: Property 'public' - Uses oneOf schema (complex, 2 variants)

### Index 432: issues/add-labels
Path: POST /repos/{owner}/{repo}/issues/{issue_number}/labels

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 5 variants)

### Index 436: issues/create
Path: POST /repos/{owner}/{repo}/issues

Issues detected:
- RequestBody schema issue in application/json: Property 'title' - Uses oneOf schema (complex, 2 variants)
- RequestBody schema issue in application/json: Property 'milestone' - Uses oneOf schema (complex, 2 variants)
- RequestBody schema issue in application/json: Property 'labels' - Array items - Uses oneOf schema (complex, 2 variants)

### Index 469: issues/set-labels
Path: PUT /repos/{owner}/{repo}/issues/{issue_number}/labels

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 5 variants)

### Index 471: issues/update
Path: PATCH /repos/{owner}/{repo}/issues/{issue_number}

Issues detected:
- RequestBody schema issue in application/json: Property 'title' - Uses oneOf schema (complex, 2 variants)
- RequestBody schema issue in application/json: Property 'milestone' - Uses oneOf schema (complex, 2 variants)
- RequestBody schema issue in application/json: Property 'labels' - Array items - Uses oneOf schema (complex, 2 variants)

### Index 479: markdown/render-raw
Path: POST /markdown/raw

Issues detected:
- Schema-example mismatch in text/plain: Schema type is string but example is an object
- Schema-example mismatch in text/x-markdown: Schema type is string but example is an object
- Non-JSON content types may cause issues

### Index 517: orgs/convert-member-to-outside-collaborator
Path: PUT /orgs/{org}/outside_collaborators/{username}

Issues detected:
- Schema-example mismatch in application/json: Schema type is object but example is not an object

### Index 520: orgs/create-or-update-custom-properties
Path: PATCH /orgs/{org}/properties/schema

Issues detected:
- RequestBody schema issue in application/json: Property 'properties' - Array items - Property 'default_value' - Uses oneOf schema (complex, 2 variants)

### Index 521: orgs/create-or-update-custom-properties-values-for-repos
Path: PATCH /orgs/{org}/properties/values

Issues detected:
- RequestBody schema issue in application/json: Property 'properties' - Array items - Property 'value' - Uses oneOf schema (complex, 2 variants)

### Index 522: orgs/create-or-update-custom-property
Path: PUT /orgs/{org}/properties/schema/{custom_property_name}

Issues detected:
- RequestBody schema issue in application/json: Property 'default_value' - Uses oneOf schema (complex, 2 variants)

### Index 523: orgs/create-webhook
Path: POST /orgs/{org}/hooks

Issues detected:
- RequestBody schema issue in application/json: Property 'config' - Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 586: orgs/update-webhook
Path: PATCH /orgs/{org}/hooks/{hook_id}

Issues detected:
- RequestBody schema issue in application/json: Property 'config' - Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 587: orgs/update-webhook-config-for-org
Path: PATCH /orgs/{org}/hooks/{hook_id}/config

Issues detected:
- RequestBody schema issue in application/json: Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 622: projects/create-card
Path: POST /projects/columns/{column_id}/cards

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 667: pulls/request-reviewers
Path: POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses anyOf schema (complex, 2 variants)

### Index 702: repos/add-status-check-contexts
Path: POST /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 703: repos/add-team-access-restrictions
Path: POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 718: repos/create-deployment
Path: POST /repos/{owner}/{repo}/deployments

Issues detected:
- RequestBody schema issue in application/json: Property 'payload' - Uses oneOf schema (complex, 2 variants)

### Index 726: repos/create-or-update-custom-properties-values
Path: PATCH /repos/{owner}/{repo}/properties/values

Issues detected:
- RequestBody schema issue in application/json: Property 'properties' - Array items - Property 'value' - Uses oneOf schema (complex, 2 variants)

### Index 729: repos/create-org-ruleset
Path: POST /orgs/{org}/rulesets

Issues detected:
- RequestBody schema issue in application/json: Property 'conditions' - Uses oneOf schema (complex, 3 variants)
- RequestBody schema issue in application/json: Property 'conditions' - oneOf[0] - Uses allOf schema (complex)
- RequestBody schema issue in application/json: Property 'conditions' - oneOf[1] - Uses allOf schema (complex)
- RequestBody schema issue in application/json: Property 'conditions' - oneOf[2] - Uses allOf schema (complex)
- RequestBody schema issue in application/json: Property 'rules' - Array items - Uses oneOf schema (complex, 21 variants)

### Index 731: repos/create-pages-site
Path: POST /repos/{owner}/{repo}/pages

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses anyOf schema (complex, 2 variants)

### Index 733: repos/create-repo-ruleset
Path: POST /repos/{owner}/{repo}/rulesets

Issues detected:
- RequestBody schema issue in application/json: Property 'rules' - Array items - Uses oneOf schema (complex, 21 variants)

### Index 736: repos/create-webhook
Path: POST /repos/{owner}/{repo}/hooks

Issues detected:
- RequestBody schema issue in application/json: Property 'config' - Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 871: repos/remove-status-check-contexts
Path: DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 873: repos/remove-team-access-restrictions
Path: DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 880: repos/set-status-check-contexts
Path: PUT /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 881: repos/set-team-access-restrictions
Path: PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 2 variants)

### Index 889: repos/update-information-about-pages-site
Path: PUT /repos/{owner}/{repo}/pages

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses anyOf schema (complex, 5 variants)
- RequestBody schema issue in application/json: Property 'source' - Uses anyOf schema (complex, 2 variants)

### Index 891: repos/update-org-ruleset
Path: PUT /orgs/{org}/rulesets/{ruleset_id}

Issues detected:
- RequestBody schema issue in application/json: Property 'conditions' - Uses oneOf schema (complex, 3 variants)
- RequestBody schema issue in application/json: Property 'conditions' - oneOf[0] - Uses allOf schema (complex)
- RequestBody schema issue in application/json: Property 'conditions' - oneOf[1] - Uses allOf schema (complex)
- RequestBody schema issue in application/json: Property 'conditions' - oneOf[2] - Uses allOf schema (complex)
- RequestBody schema issue in application/json: Property 'rules' - Array items - Uses oneOf schema (complex, 21 variants)

### Index 895: repos/update-repo-ruleset
Path: PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}

Issues detected:
- RequestBody schema issue in application/json: Property 'rules' - Array items - Uses oneOf schema (complex, 21 variants)

### Index 897: repos/update-webhook
Path: PATCH /repos/{owner}/{repo}/hooks/{hook_id}

Issues detected:
- RequestBody schema issue in application/json: Property 'config' - Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 898: repos/update-webhook-config-for-repo
Path: PATCH /repos/{owner}/{repo}/hooks/{hook_id}/config

Issues detected:
- RequestBody schema issue in application/json: Property 'insecure_ssl' - Uses oneOf schema (complex, 2 variants)

### Index 899: repos/upload-release-asset
Path: POST /repos/{owner}/{repo}/releases/{release_id}/assets

Issues detected:
- Non-JSON content types may cause issues

### Index 921: security-advisories/list-global-advisories
Path: GET /advisories

Issues detected:
- Parameter[5] schema issue: Uses oneOf schema (complex, 2 variants)
- Parameter[7] schema issue: Uses oneOf schema (complex, 2 variants)

### Index 985: users/add-email-for-authenticated-user
Path: POST /user/emails

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 3 variants)

### Index 994: users/delete-email-for-authenticated-user
Path: DELETE /user/emails

Issues detected:
- Schema-example mismatch in application/json: Complex schema type may cause validation issues
- RequestBody schema issue in application/json: Uses oneOf schema (complex, 3 variants)

