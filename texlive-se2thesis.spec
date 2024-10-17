Name:		texlive-se2thesis
Version:	72025
Release:	1
Summary:	A Thesis Class for the Chair of Software Engineering II at the University of Passau, Germany
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/se2thesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/se2thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/se2thesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/se2thesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The se2thesis bundle provides a document class for writing a
theses with the Chair of Software Engineering II at the
University of Passau, Germany. The class is based on Markus
Kohm's KOMA-Script classes and provides several additions and
customizations to these classes. While the class provides some
basic settings, mostly regrading the type area, fonts, and the
title page, it still provides large degrees of freedom to its
users. However, the package's documentation also provides
recommendations regarding several aspects, for example,
recommending BibLaTeX for bibliographies.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/se2thesis
%{_texmfdistdir}/tex/latex/se2thesis
%doc %{_texmfdistdir}/doc/latex/se2thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
