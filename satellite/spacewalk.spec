%define release_name Alpha
Name:           spacewalk
Version:        0.2.1
Release:        4%{?dist}
Summary:        Spacewalk Systems Management Application
Group:          Applications/Internet
License:        GPLv2
BuildRoot:      %{_tmppath}/%{name}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python
Requires:       python >= 2.3
Requires:       spacewalk-setup

# Java
Requires:       spacewalk-java
Requires:       spacewalk-taskomatic
Requires:       spacewalk-search

# Perl
Requires:       spacewalk-html
Requires:       spacewalk-base
Requires:       spacewalk-dobby
Requires:       spacewalk-cypress
Requires:       spacewalk-grail
Requires:       spacewalk-pxt
Requires:       spacewalk-sniglets
Requires:       spacewalk-moon

# Python
Requires:       spacewalk-certs-tools
Requires:       spacewalk-backend
Requires:       spacewalk-backend-app
Requires:       spacewalk-backend-applet
Requires:       spacewalk-backend-config-files
Requires:       spacewalk-backend-config-files-common
Requires:       spacewalk-backend-config-files-tool
Requires:       spacewalk-backend-package-push-server
Requires:       spacewalk-backend-satellite-tools
Requires:       spacewalk-backend-server
Requires:       spacewalk-backend-sql
Requires:       spacewalk-backend-xml-export-libs
Requires:       spacewalk-backend-xmlrpc
Requires:       spacewalk-backend-xp
Requires:       rhnpush


# Misc
Requires:       spacewalk-schema
Requires:       spacewalk-config

# Requires:       osa-dispatcher
# Requires:       jabberpy

# Monitoring support 

# Requires:       perl-Apache-Admin-Config
# Requires:       perl-Apache-DBI
# Requires:       perl-Class-MethodMaker
# Requires:       perl-Config-IniFiles
# Requires:       perl-Crypt-GeneratePassword
# Requires:       perl-FreezeThaw
# Requires:       perl-HTML-TableExtract
# Requires:       perl-IO-Capture
# Requires:       perl-IO-Socket-SSL
# Requires:       perl-IO-stringy
# Requires:       perl-Mail-Alias
# Requires:       perl-MailTools
# Requires:       perl-MIME-tools
# Requires:       perl-Net-SNMP
# Requires:       perl-Network-IPv4Addr
# Requires:       perl-XML-Generator
# Requires:       perl-CGI-mp20

# Monitoring packages
# Requires:       bdb_perl
# Requires:       oracle_perl
# Requires:       ConfigPusher-general
# Requires:       eventReceivers
# Requires:       MessageQueue
# Requires:       NOCpulsePlugins
# Requires:       NPalert
# Requires:       np-config
# Requires:       NPusers
# Requires:       nslogs
# Requires:       perl-NOCpulse-CLAC
# Requires:       perl-NOCpulse-Debug
# Requires:       perl-NOCpulse-Gritch
# Requires:       perl-NOCpulse-Object
# Requires:       perl-NOCpulse-OracleDB
# Requires:       perl-NOCpulse-PersistentConnection
# Requires:       perl-NOCpulse-Probe
# Requires:       perl-NOCpulse-ProcessPool
# Requires:       perl-NOCpulse-Scheduler
# Requires:       perl-NOCpulse-SetID
# Requires:       perl-NOCpulse-Utils
# Requires:       ProgAGoGo
# Requires:       SatConfig-bootstrap
# Requires:       SatConfig-bootstrap-server
# Requires:       SatConfig-cluster
# Requires:       SatConfig-dbsynch
# Requires:       SatConfig-generator
# Requires:       SatConfig-installer
# Requires:       SatConfig-spread
# Requires:       scdb
# Requires:       scdb_accessor_perl
# Requires:       SNMPAlerts
# Requires:       SputLite-client
# Requires:       SputLite-server
# Requires:       ssl_bridge
# Requires:       status_log_acceptor
# Requires:       tsdb
# Requires:       tsdb_accessor_perl

# Solaris
# Requires:       rhn-solaris-bootstrap
# Requires:       rhn_solaris_bootstrap_5_1_0_3



%description
Spacewalk is a systems management application that will 
inventory, provision, update and control your Linux and 
Solaris machines.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
echo "Spacewalk release %{version} (%{release_name})" > $RPM_BUILD_ROOT/%{_sysconfdir}/spacewalk-release

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/%{_sysconfdir}/spacewalk-release

%changelog
* Tue Sep  2 2008 Jesus Rodriguez <jesusr@redhat.com>
- add spacewalk-search as a new Requires
- change version to work with the new make srpm rules

* Mon Sep  1 2008 Milan Zazrivec <mzazrivec@redhat.com> 0.2-4
- bumped minor release for new package build

* Wed Aug 13 2008 Mike 0.2-3
- Fixing requires for new package names

* Mon Aug 11 2008 Mike 0.2-2
- tag to rebuild

* Wed Aug  6 2008 Jan Pazdziora 0.1-7
- tag to rebuild

* Mon Aug  4 2008 Miroslav Suchy <msuchy@redhat.com>
- Migrate name of packages to spacewalk namespace.

* Tue Jun 3 2008 Jesus Rodriguez <mmccune at redhat dot com> 0.1
- initial rpm release
