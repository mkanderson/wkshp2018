### Agenda

---

#### Introduction

---

#### Meet the Shell

ex.1
```
for i in $(do_some_stuff); do
  eat cookie
done
```
Note: This is a typical Bash error trap..

>>>

ex.1
```
for i in $(do_some_stuff); do
  eat cookie
done
```

---

Some code:

```
#!/usr/bin/perl -w
# Call a PostgreSQL client program with the version, cluster and default
# database specified in ~/.postgresqlrc or
# /etc/postgresql-common/user_clusters.
#
# (C) 2005-2009 Martin Pitt <mpitt@debian.org>
# (C) 2013-2014 Christoph Berg <myon@debian.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

use strict;
use POSIX;
use PgCommon;

my ($version, $cluster, $db, $port, $host);

$host = $ENV{'PGHOST'};

# Check for PGCLUSTER in %ENV
if (defined $ENV{'PGCLUSTER'}) {
    ($version, $cluster) = split ('/', $ENV{'PGCLUSTER'}, 2);
    error 'Invalid version specified with $PGCLUSTER' unless version_exists $version;
    error 'No cluster specified with $PGCLUSTER' unless $cluster;
}

# Check for --cluster argument and filter it out, and check if --port is specified
my $port_specified = exists $ENV{'PGPORT'};
for (my $i = 0; $i <= $#ARGV; ++$i) {
    last if $ARGV[$i] eq '--';

    if ($ARGV[$i] eq '--cluster') {
        error '--cluster option needs an argument (<version>/<cluster>)' if ($i >= $#ARGV);

        ($version, $cluster) = split ('/', $ARGV[$i+1], 2);
	$host = undef; # --cluster overrides $PGHOST env var
        error 'Invalid version specified with --cluster' unless version_exists $version;
        error 'No cluster specified with --cluster' unless $cluster;

        splice @ARGV, $i, 2;
        last;
    } elsif ($ARGV[$i] =~ /^--cluster=(\d+\.\d)\/(.+)/) {
        ($version, $cluster) = ($1, $2);
        $host = undef; # --cluster overrides $PGHOST env var
        error 'Invalid version specified with --cluster' unless version_exists $version;
        error 'No cluster specified with --cluster' unless $cluster;

        splice @ARGV, $i, 1;
        last;
    }

    $port_specified = 1 if $ARGV[$i] =~ /^--port\b/ || $ARGV[$i] =~ /^-\w*p\w*\d*$/;
    $host = '.from.commandline' if $ARGV[$i] =~ /^--host\b/ || $ARGV[$i] =~ /^-\w*h\w*$/;
}

# Determine $version, $cluster, $db, $port from map files
($version, $cluster, $db) = user_cluster_map() unless $cluster;

# check if we have a network cluster
if (!$host && $cluster && !cluster_exists $version, $cluster) {
    if ($cluster =~ /^(\S+):(\d*)$/) {
	$host = $1;
	$port = $2 || 5432;
    } else {
	error 'Specified cluster does not exist locally and does not specify a remote cluster';
    }
}

if (!$host && $cluster) {
    $port = get_cluster_port($version, $cluster);

    unless ($ENV{'PGHOST'}) {
        # default to cluster specific Unix socket directory
        $ENV{'PGHOST'} = get_cluster_socketdir $version, $cluster;
    }
}

$ENV{'PGSYSCONFDIR'} = '/etc/postgresql-common' if !$ENV{'PGSYSCONFDIR'};
$ENV{'PGPORT'} = $port if $port && !$ENV{'PGPORT'};
$ENV{'PGDATABASE'} = $db if $db && !$ENV{'PGDATABASE'};
$ENV{'PGHOST'} = $host if $host && $host ne '.from.commandline';

# if we only have a port, but no version here, use the latest version
# TODO: this could be improved by better argument parsing and mapping back the
# port to a cluster version/name
if (!$version and $port_specified) {
    $version = get_newest_version;
}

unless ($version) {
    if (get_versions) {
	error 'No existing local cluster is suitable as a default target. Please see man pg_wrapper(1) how to specify one.';
    } else {
	error 'You must install at least one postgresql-client-<version> package.';
    }
}

error 'Invalid PostgreSQL cluster version' unless -d "$PgCommon::binroot$version";
my $cmdname = (split '/', $0)[-1];
my $cmd;

# for psql we always want the latest version, as this is backwards compatible
# to every major version that that we support
if ($cmdname eq 'pg_wrapper') {
    error "pg_wrapper should not be called directly, but through a symlink";
} elsif ($cmdname =~ /^(psql|pg_archivecleanup|pg_isready)$/) {
    $cmd = get_program_path ($cmdname, get_newest_version);
} else {
    $cmd = get_program_path ($cmdname, $version);
}

# libreadline is a lot better than libedit, so prefer that
if ($cmdname eq 'psql' and not $PgCommon::rpm) {
    my @readlines;
    # non-multiarch path
    @readlines = sort(</lib/libreadline.so.?>);

    unless (@readlines) {
	# get multiarch dir for our architecture
	if (open PS, '-|', '/usr/bin/ldd', $cmd) {
	    my $out;
	    read PS, $out, 10000;
	    close PS;
	    if ($out =~ m!/libreadline.so!) {
		# already linked against libreadline
		@readlines = ();
	    }
	    else
	    {
		my ($lib_path) = $out =~ m!(/lib/.*)/libedit.so!;

		@readlines = sort(<$lib_path/libreadline.so.?>);
	    }
	}
    }

    if (@readlines) {
	$ENV{'LD_PRELOAD'} = ($ENV{'LD_PRELOAD'} or '') . ':' . $readlines[-1];
    }
}

error "pg_wrapper: $cmdname was not found in $PgCommon::binroot$version/bin" unless $cmd;
unshift @ARGV, $cmd;
exec @ARGV;



```
