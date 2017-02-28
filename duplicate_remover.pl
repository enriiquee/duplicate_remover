#!/usr/bin/perl

use warnings;
use strict;

my %seen; 
my $count = 0; 
my $output; 

while (  <> ) {
  next if ( m/spectrum=(\d+)/ and $seen{$1}++ );
  print;
}