%global tl_name parnotes
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3c
Release:	%{tl_revision}.1
Summary:	Notes after every paragraph (or elsewhere)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parnotes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parnotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the \parnote command. The notes are set as (normal)
running paragraphs; placement is at the end of each paragraph, or
manually, using the \parnotes command.

