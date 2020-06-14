# uscis-case-query

**Introduction**

uscis-case-query is a small tool to query USCIS case by using the receipt number under command line.

**Usage**

```
usage: uscis_case_query.py [-h] -c CASE

USCIS Case Query Tool

optional arguments:
  -h, --help            show this help message and exit
  -c CASE, --case CASE  USCIS receipt number
```

*-c*: USCIS receipt number

**Example**

```
$ python3 uscis_case_query.py -c LIN0000000000
LIN0000000000: Case Was Received At My Local Office

On March 16, 2018, we received your Form I-751, Petition to Remove Conditions on Residence, Receipt Number LIN0000000000, at your local office. If you move, go to www.uscis.gov/addresschange to give us your new mailing address.
```

**Notes**
* If user would like to query a bunch of USCIS receipt numbers in UNIX-like environment, user can use `xargs` command to query the results. Example:

```
$ cat uscis_case_list | xargs -I {} uscis_case_query.py -c {}
```

**Change Log**

**20190126** initial commit

**20200613** added case status text block
