# Satellite / Capsule patching

Patches a RHEL Satellite server and its Capsules via `satellite-maintain`.
Satellite is always patched first; the Capsules play only starts if that
play succeeds, then patches capsules one at a time (`serial: 1`) and stops
the rollout if any capsule comes back unhealthy.

## Layout

```
.
├── ansible.cfg
├── inventory/hosts.ini            # replace with real hostnames, or point AAP at its own Inventory instead
├── group_vars/all.yml             # tunables: health-check whitelist, reboot policy, backup toggle
├── collections/requirements.yml   # synced by AAP's Project update step
├── patch_satellite_capsules.yml   # the playbook
└── aap/survey_spec.json           # importable Job Template survey (optional vars)
```

## Running locally

```
ansible-playbook patch_satellite_capsules.yml
ansible-playbook patch_satellite_capsules.yml --limit capsules
```

## Running from AAP

1. **Project**: SCM type Git, pointing at this repo. AAP will run the
   `collections/requirements.yml` sync automatically.
2. **Inventory**: either sync `inventory/hosts.ini` in as a Project-backed
   inventory source, or create an AAP Inventory with two groups named
   `satellite` (1 host) and `capsules` (5 hosts) — the playbook only cares
   about those group names.
3. **Credentials**: attach a Machine credential with SSH + become
   (sudo/root) access to all 6 hosts. Don't put the hammer username/password
   in `group_vars` — if you enable the optional capsule sync check, supply
   `hammer_username`/`hammer_password` via the survey below or a Vault
   credential, not committed vars.
4. **Job Template**: playbook = `patch_satellite_capsules.yml`, enable
   privilege escalation, attach the credentials from step 3.
   - Import `aap/survey_spec.json` as the template's survey to expose
     `satellite_take_backup`, `capsule_check_sync_status`,
     `hammer_username`/`hammer_password`, and
     `satellite_maintain_update_extra_args` as run-time prompts.
   - To patch only the capsules once Satellite is confirmed healthy, set
     the Job Template's **Limit** field to `capsules`.
5. Optionally split this into two Job Templates (`Patch Satellite`,
   `Patch Capsules`) chained in a Workflow Job Template if you want a manual
   approval gate between the two stages.

## Notes

- Satellite ≤ 6.10 uses `foreman-maintain` instead of `satellite-maintain`
  — swap the command name throughout `patch_satellite_capsules.yml` if
  that's your version.
- Reboots are automatic when `needs-restarting -r` says one is needed;
  disable via `satellite_reboot_when_required: false` in `group_vars/all.yml`
  or as an extra var.
