%global tl_name se2thesis
%global tl_revision 78585

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.4.1
Release:	%{tl_revision}.1
Summary:	A Thesis Class for the Chair of Software Engineering II at the University of ...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/se2thesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/se2thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/se2thesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/se2thesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The se2thesis bundle provides a document class for writing a theses with
the Chair of Software Engineering II at the University of Passau,
Germany. The class is based on Markus Kohm's KOMA-Script classes and
provides several additions and customizations to these classes. While
the class provides some basic settings, mostly regrading the type area,
fonts, and the title page, it still provides large degrees of freedom to
its users. However, the package's documentation also provides
recommendations regarding several aspects, for example, recommending
BibLaTeX for bibliographies.

