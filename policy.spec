# enter date when you got the policy
%define	snap	20031226
Summary:	SELinux example policy configuration
Summary(pl):	Przyk³adowa konfiguracja polityki SELinuksa
Name:		policy
Version:	1.4_%{snap}
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.coker.com.au/selinux/%{name}.tgz
# Source0-md5:	1f7cbff059f5e0e549fd68d351eb5c71
Patch0:		%{name}-rhat.patch
BuildRequires:	checkpolicy
BuildRequires:	m4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains the SELinux example policy configuration along
with the Flask configuration information and the application
configuration files.

%description -l pl
Security-enhanced Linux jest poprawk± j±dra Linuksa i wielu
aplikacji u¿ytkowych o funkcjach podwy¿szonego bezpieczeñstwa.
Zaprojektowany jest tak, aby w prosty sposób ukazaæ znaczenie
mandatowej kontroli dostêpu dla spo³eczno¶ci Linuksowej. Ukazuje
równie¿ jak tak± kontrolê mo¿na dodaæ do istniej±cego systemu typu
Linux. J±dro SELinux zawiera nowe sk³adniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeñstwa systemu operacyjnego
Flask. Te elementy zapewniaj± ogólne wsparcie we wdra¿aniu wielu typów
polityk mandatowej kontroli dostêpu, w³±czaj±c te wzorowane na: Type
Enforcement, kontroli dostêpu opartej na rolach i zabezpieczeniach
wielopoziomowych.

Ten pakiet zawiera przyk³adow± konfiguracjê polityki dla SELinuksa
wraz z informacjami o konfiguracji Flask oraz plikami konfiguracyjnymi
aplikacji.

%package sources
Summary:	SELinux example policy configuration source files
Summary(pl):	Pliki ¼ród³owe przyk³adowej konfiguracji polityki SELinuksa
Group:		Base
Requires:	m4
Requires:	make
Requires:	policycoreutils

%description sources
This subpackage includes the source files used to build the policy
configuration. Includes policy.conf and the Makefiles, macros and
source files for it.

%description sources -l pl
Ten podpakiet zawiera pliki ¼ród³owe u¿yte do zbudowania konfiguracji
polityki. Zawiera policy.conf oraz wszystkie Makefile, makra i pliki
¼ród³owe.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} policy

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/security/selinux

%{__make} install install-src \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/security/selinux/src/policy/{COPYING,ChangeLog,README,VERSION,policy.spec,policy.15}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/security/selinux
%{_sysconfdir}/security/selinux/policy.*
%{_sysconfdir}/security/*_*

%files sources
%defattr(644,root,root,755)
%doc ChangeLog README
# XXX: duplicate
%dir %{_sysconfdir}/security/selinux
%dir %{_sysconfdir}/security/selinux/src
%{_sysconfdir}/security/selinux/src/policy.conf
%dir %{_sysconfdir}/security/selinux/src/policy
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/selinux/src/policy/users
%{_sysconfdir}/security/selinux/src/policy/[!u]*
