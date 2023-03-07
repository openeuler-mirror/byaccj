Name:		byaccj
Version:	1.15
Release:	21
Summary:	BYACC/J Java extension
License:	Public Domain
URL:		http://byaccj.sourceforge.net/
Source0:	http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz
Patch0:         fix-add-the-compilation-option-pie.patch

BuildRequires:  make gdb-headless gcc

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible parser generator.
Standard YACC takes a YACC source file, and generates one or more C files from it,
which if compiled properly, will produce a LALR-grammar parser.
This is useful for expression parsing, interactive command parsing, and file reading.
Many megabytes of YACC code have been written over the years.
This is the standard YACC tool that is in use every day to produce C/C++ parsers.
I have added a "-J" flag which will cause BYACC to generate Java source code, instead.
So there finally is a YACC for Java now! 

%package	help
Summary:	Help document for the byaacj package

%description	help
Help document for the byaacj package

%prep
%autosetup -n %{name}%{version} -p1
chmod -c 644 src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4||g' src/Makefile

%build
cd src
%make_build yacc CFLAGS="%{optflags}"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 src/yacc %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%files help
%doc docs/* src/README

%changelog
* Fri Mar 03 2023 wulei <wulei80@h-partners.com> - 1.15-21
- Add the compilation option pie

* Mon May 31 2021 baizhonggui <baizhonggui@huawei.com> - 1.15-20
- Fix building error: cc: No such file or directory
- Add gcc in BuildRequires

* Sun Mar 15 2020 zhangtao<zhangtao221@huawei.com> - 1.15-19
- Package init

