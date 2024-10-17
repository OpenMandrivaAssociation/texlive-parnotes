Name:		texlive-parnotes
Version:	71505
Release:	1
Summary:	Notes after every paragraph (or elsewhere)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parnotes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the \parnote command. The notes are set as
(normal) running paragraphs; placement is at the end of each
paragraph, or manually, using the \parnotes command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parnotes
%doc %{_texmfdistdir}/doc/latex/parnotes

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
