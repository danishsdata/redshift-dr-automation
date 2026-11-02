# redshift-dr-automation

A Step Functions run for Redshift disaster recovery: snapshot the
production cluster, wait, check the snapshot is available, restore it to
a DR cluster, and send an SNS message with the result. Any step failing
goes straight to the failure notification.

Portfolio implementation of patterns I use as an AWS DBA / data engineer.

## Why

A snapshot nobody has restored is a guess. The restore step is the whole
point: it proves the backup works before you need it for real.

## Run

1. Deploy snapshot.py, restore.py, and notify.py as three Lambdas.
2. Put state_machine.json in Step Functions, filling in the three
   function names.
3. Schedule it nightly with EventBridge, passing the production cluster
   id, the DR cluster id, and a dated snapshot id.
