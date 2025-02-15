# Votes

The Vote entity represents the number of votes a candidate has received in a specific precinct. Each vote entry is uniquely identified and is linked to a candidate, a precinct, and a barangay. The `votes_count` attribute keeps track of the total votes for the candidate within the precinct.

## JSON Format

| Name         | Type    | Read-only | Mandatory | Description                                              |
| ------------ | ------- | --------- | --------- | -------------------------------------------------------- |
| id           | string  | true      | false     | Unique vote entry identifier                             |
| candidate_id | string  | true      | true      | Reference to the candidate receiving votes               |
| precinct_id  | string  | true      | true      | Reference to the precinct where votes were cast          |
| barangay_id  | string  | true      | true      | Reference to the barangay associated with the vote entry |
| votes_count  | integer | false     | true      | Total votes recorded for the candidate in this precinct  |
| updated_at   | string  | true      | false     | Timestamp of the last vote update                        |
