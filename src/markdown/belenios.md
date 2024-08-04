---
date: 2024-08-04
title: Belenios
description: A modern voting system for the modern age
author: Shinji Pons
---

# Belenios

Belenios aims at providing an easy to use voting system, guaranteeing state-of-the-art security, namely vote privacy and verifiability. It can be used in many types of elections (including referendums), ranging from scientific councils to sport associations.

- **Vote privacy:** no one can learn the vote of a voter. Vote privacy relies on the encryption of the votes.
- **Verifiablity:** Every voter can check that her vote has been counted and only eligible voters may vote. Verifiablity relies on the fact that the ballot box is public (voters can check that their ballots have been received) and on the fact that the tally is publicly verifiable (anyone can recount the votes). Moreover, ballots are signed by the voter credential (only eligible voters are able vote).

# Release of Belenios 2.5.1

The main goal of this release is to correct an issue raised by Olivier Pereira regarding the implementation of the Distributed Key Generation (DKG) scheme in the threshold mode, that is when the election key is distributed among n trustees, with a threshold of k trustees to decrypt the election. This is now fixed by adding an extra signature field. As a side effect, new elections should be monitored with this additional signature check and our verification tools have been updated accordingly. We are very grateful to Olivier Pereira for reporting this issue.

!(This is a test image)[https://ichef.bbci.co.uk/news/1536/cpsprodpb/817f/live/e617c330-526b-11ef-8671-d1d197619874.jpg.webp]