"""Wait until a Redshift snapshot is available, then report its status.

Polls describe_cluster_snapshots. Exits non-zero if the snapshot ends up
in failed status or the wait runs out, so the state machine routes to
the failure notification instead of restoring a bad snapshot.
"""

import argparse
import sys
import time

import boto3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--timeout-minutes", type=int, default=60)
    parser.add_argument("--poll-seconds", type=int, default=60)
    args = parser.parse_args()

    client = boto3.client("redshift")
    deadline = time.time() + args.timeout_minutes * 60
    while time.time() < deadline:
        resp = client.describe_cluster_snapshots(
            SnapshotIdentifier=args.snapshot_id
        )
        snaps = resp.get("Snapshots", [])
        if snaps:
            status = snaps[0]["Status"]
            print(args.snapshot_id, status)
            if status == "available":
                return 0
            if status == "failed":
                return 1
        time.sleep(args.poll_seconds)
    print(args.snapshot_id, "timed out waiting for available")
    return 1


if __name__ == "__main__":
    sys.exit(main())
