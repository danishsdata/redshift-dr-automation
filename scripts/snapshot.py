"""Create a manual snapshot of a Redshift cluster."""

import argparse

import boto3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cluster", required=True)
    parser.add_argument("--snapshot-id", required=True)
    args = parser.parse_args()

    client = boto3.client("redshift")
    resp = client.create_cluster_snapshot(
        SnapshotIdentifier=args.snapshot_id,
        ClusterIdentifier=args.cluster,
    )
    snap = resp["Snapshot"]
    print(snap["SnapshotIdentifier"], snap["Status"])


if __name__ == "__main__":
    main()
