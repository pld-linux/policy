%define	snap	20031226
Summary:	SELinux example policy configuration
Name:		policy
# enter date when you got the policy
%define snap    20031226
Version:	1.4_%{snap}
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.coker.com.au/selinux/%{name}.tgz
# Source0-md5:	1f7cbff059f5e0e549fd68d351eb5c71
Patch0:		%{name}-rhat.patch
BuildRequires:	m4
BuildRequires:	checkpolicy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Security-enhanced Linux is a patch of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement®, Role-based Access Control, and
Multi-level Security.

This package contains the SELinux example policy configuration along
with the Flask configuration information and the application
configuration files.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} policy

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/security/selinux

%{__make} install install-src \
	DESTDIR="${RPM_BUILD_ROOT}" install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/security/selinux
%{_sysconfdir}/security/selinux/policy.*
%{_sysconfdir}/security/*_*

%package sources
Summary:	SELinux example policy configuration source files
Group:		Base
Requires:	m4
Requires:	policycoreutils
Requires:	make

%description sources
This subpackage includes the source files used to build the policy
configuration. Includes policy.conf and the Makefiles, macros and
source files for it.

%files sources
%defattr(644,root,root,755)
%dir %{_sysconfdir}/security/selinux
%dir %{_sysconfdir}/security/selinux/src
%{_sysconfdir}/security/selinux/src/policy.conf
%config(noreplace) %{_sysconfdir}/security/selinux/src/policy/users
%{_sysconfdir}/security/selinux/src/policy/*
