"""Restore a Redshift cluster from a snapshot.

Used for DR drills: restore into a separate cluster id so the production
cluster is never touched.
"""

import argparse

import boto3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--new-cluster-id", required=True)
    parser.add_argument("--node-type", default="ra3.xlplus")
    parser.add_argument("--number-of-nodes", type=int, default=2)
    args = parser.parse_args()

    client = boto3.client("redshift")
    resp = client.restore_from_cluster_snapshot(
        ClusterIdentifier=args.new_cluster_id,
        SnapshotIdentifier=args.snapshot_id,
        NodeType=args.node_type,
        NumberOfNodes=args.number_of_nodes,
    )
    cluster = resp["Cluster"]
    print(cluster["ClusterIdentifier"], cluster["ClusterStatus"])


if __name__ == "__main__":
    main()
