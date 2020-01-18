Name:       perl-srpm-macros    
Version:    1
Release:    7%{?dist}
Summary:    RPM macros for building Perl source package from source repository
Group:      Development/Libraries
License:    GPLv3+
Source0:    macros.perl-srpm
BuildArch:  noarch

%description
These RPM macros are used for building Perl source packages from source
repositories. They influence build-requires set into the source package.

%install
install -m 644 -D "%{SOURCE0}" \
    "$RPM_BUILD_ROOT/%{_sysconfdir}/rpm/macros.perl-srpm"

%files
%{_sysconfdir}/rpm/macros.perl-srpm

%changelog
* Thu Feb 28 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1-7
- Remove %%config from %%{_sysconfdir}/rpm/macros.*
  (https://fedorahosted.org/fpc/ticket/259).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1-4
- Disable perl_bootstrap for perl 5.16 rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1-3
- Perl 5.16 rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1-2
- Enable perl_bootstrap for perl 5.16 rebuild

* Tue May 15 2012 Petr Pisar <ppisar@redhat.com> - 1-1
- Introduce Perl SRPM macros as a standalone package


