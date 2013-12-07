# do not provide/require private perl modules
%if %{_use_internal_dependency_generator}
%define __noautoreq 'GD\\.so|perl\\(HTML::Clean\\)|perl\\(WML::GD\\)'
%define __noautoprov 'GD\\.so|perl\\(HTML::Clean\\)|perl\\(WML::GD\\)'
%else
%define _requires_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)
%define _provides_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)
%endif

Summary:	Website META Language
Name:		wml
Version:	2.2.2
Release:	4
License:	GPLv2+
Group:		Publishing
URL:		http://thewml.org/
Source:		https://bitbucket.org/shlomif/website-meta-language/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	libtool
BuildRequires:	libltdl-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
# (tpg) use system version not the pulled in here
#BuildRequires:	db-devel
# (crisb) doesnt seem to pull in the db-devel package so spec here
BuildRequires:	db53-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	lynx
BuildRequires:	perl-Bit-Vector >= 5.2
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(GD)
BuildRequires:	perl(Getopt::Long) >= 2.16
BuildRequires:	perl(HTML::Clean)
BuildRequires:	perl(Image::Size) >= 2.6
BuildRequires:	perl(IO::File) >= 1.07
BuildRequires:	perl(Term::ReadKey) >= 2.11
Requires:	perl(Bit::Vector) >= 5.2
Requires:	perl(File::Spec)
Requires:	perl(Getopt::Long) >= 2.16
Requires:	perl(Image::Size) >= 2.6
Requires:	perl(IO::File) >= 1.07
Requires:	perl(Term::ReadKey) >= 2.11

%description
WML is a free and extensible Webdesigner's off-line HTML generation
toolkit for Unix, distributed under the GNU General Public License
(GPL v2). It is written in ANSI C and Perl 5, build via a GNU Autoconf
based source tree and runs out-of-the-box on all major Unix derivatives.
It can be used free of charge both in educational and commercial
environments.

%prep
%setup -q

%build
%cmake -DLIB_INSTALL_DIR=%{_libdir} -DLOCALE_INSTALL_DIR=%{_datadir}/locale
%make

# TODO : add percent-check once it is working.

%install
%makeinstall_std -C build

%files
%doc ANNOUNCE BUGREPORT ChangeLog COPYING COPYRIGHT COPYRIGHT.OTHER CREDITS 
%doc NEWS README SUPPORT VERSION VERSION.HISTORY
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*

%changelog
* Fri Aug 24 2012 shlomif <shlomif> 2.2.0-7.mga3
+ Revision: 283629
- Rebuild for the new perl

* Fri Jun 01 2012 shlomif <shlomif> 2.2.0-6.mga3
+ Revision: 253185
- Made rpmlint happier

* Fri Jun 01 2012 shlomif <shlomif> 2.2.0-5.mga3
+ Revision: 252957
- BuildRequires on gdbm-devel and db-devel
- BuildRequires on perl(HTML::Clean)
- BuildRequires on GD.pm
- Add a missing BuildRequires on cmake
- New version: 2.2.0

* Fri Dec 16 2011 shlomif <shlomif> 2.0.11-9.mga2
+ Revision: 182723
- imported package wml


* Wed Apr 06 2011 Shlomi Fish <shlomif@mandriva.org> 2.0.11-9mdv2011.0
+ Revision: 651083
- Bump the release for the new perl

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.11-8mdv2011.0
+ Revision: 608170
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.11-7mdv2010.1
+ Revision: 524317
- rebuilt for 2010.1

* Mon Sep 28 2009 Olivier Blin <oblin@mandriva.com> 2.0.11-6mdv2010.0
+ Revision: 450404
- merge build fixes from Gentoo (Arnaud Patard):
  format errors and autotools
- build with external libltdl (from Arnaud Patard)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.11-5mdv2009.0
+ Revision: 225927
- rebuild

* Sun Mar 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.11-4mdv2008.1
+ Revision: 189571
- fix #39253 (wml is broken since the CVE fix.)

* Wed Mar 19 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.11-3mdv2008.1
+ Revision: 188821
- fix #38582, #38583 (fixes CVE-2008-0665, CVE-2008-0666)

* Thu Jan 24 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.11-2mdv2008.1
+ Revision: 157284
- perl 5.10 fixes from Shlomi (#37094)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 28 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.11-1mdv2008.0
+ Revision: 93681
- fix build requires (lynx)
- fix build requires (gettext-devel)
- 2.0.11
- bunzip and rediff patches
- link against system pcre libs (P4)
- attempt to fix #34245 (wml doesn't work on x86_64)

  + Thierry Vignaud <tv@mandriva.org>
    - s/Mandrake/Mandriva/

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.9-13mdv2008.0
+ Revision: 74822
- Import wml



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.0.9-13mdv2007.0
- Rebuild

* Sun Jun 18 2006 Stefan van der Eijk <stefan@eijk.nu> 2.0.9-12
- rebuild for png
- %%mkrel

* Sat Oct 15 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.0.9-11mdk
- fix one of the perl build dependencies, for version matching

* Wed Sep  7 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.0.9-10mdk
- gcc4 fixes

* Wed Nov 17 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.0.9-9mdk
- Rebuild for new perl

* Sun Dec 14 2003 Luca Berra <bluca@vodka.it> 2.0.9-8mdk
- fixed configure script to use 'use' instead of 'require'
- substituted deprecated File::PathConvert with Cwd and File::Spec (both bundled with perl)
- use Config{perllibs} instead of Config{libs}, kill (build)requires for gdbm/db2
- use --with-openworld, so we do not rebuild our own modules
- do not provide/require the other private perl-modules

* Thu Sep 18 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.0.9-7mdk
- BuildRequires: libgdbm-devel

* Wed Jun 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.9-6mdk
- get rid of debug stuff in %%{_libdir}
- compile with $RPM_OPT_FLAGS
- don't rm -rf $RPM_OPT_FLAGS in %%prep stage

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.9-5mdk
- rebuild for new auto{prov,req}

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 2.0.9-4mdk
- fix buildrequires

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 2.0.9-3mdk
- fix buildrequires

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 2.0.9-2mdk
- fix buildrequires

* Tue Jan 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.0.9-1mdk
- 2.0.9

* Fri Jul 12 2002 Götz Waschk <waschk@linux-mandrake.com> 2.0.8-1mdk
- buildrequires db2-devel
- patch eperl to build with perl 5.8.0
- 2.0.8

* Fri Oct 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.0.7-1mdk
- 2.0.7

* Fri Aug 31 2001 Etienne Faure <etienne@mandrakesoft.com> 2.0.6-3mdk
- rebuild

* Wed Feb 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.0.6-2mdk
- rebuild

* Wed Nov 08 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.0.6-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- 2.0.6

* Wed Sep  6 2000 Götz Waschk <waschk@linux-mandrake.com> 2.0.3-1mdk
- updated to 2.0.3
- make rpmlint happy

* Sun Jul 30 2000 Götz Waschk <waschk@linux-mandrake.com> 2.0.2-1mdk
- initial Mandrake package
