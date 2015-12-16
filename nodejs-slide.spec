%{?scl:%scl_package nodejs-slide}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-slide
Version:    1.1.6
Release:    1%{?dist}
Summary:    A flow control library that fits in a slideshow
License:    ISC
URL:        https://github.com/isaacs/slide-flow-control
Source0:    http://registry.npmjs.org/slide/-/slide-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Provides simple, easy callbacks for node.js.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/slide
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/slide

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/slide
%doc LICENSE README.md

%changelog
* Thu Jan 08 2015 Tomas Hrcka <thrcka@redhat.com> - 1.1.6-1
- New upstream release

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.1.5-2
- replace provides and requires with macro

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.5-1
- update to upstream release 1.1.5
- add ExclusiveArch logic

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-7
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-6
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.3-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-4
- add missing build section
- mention missing license

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-3
- missing package.json

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-2
- bring into conformance with newer library packaging standards
- guard Requires for F17 automatic dependency generation

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-1
- initial package
