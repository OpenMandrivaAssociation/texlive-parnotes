# revision 25032
# category Package
# catalog-ctan /macros/latex/contrib/parnotes
# catalog-date 2012-01-05 00:06:09 +0100
# catalog-license lppl1.3
# catalog-version 1
Name:		texlive-parnotes
Version:	1
Release:	3
Summary:	Notes after every paragraph (or elsewhere)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parnotes.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/parnotes/parnotes.sty
%doc %{_texmfdistdir}/doc/latex/parnotes/README
%doc %{_texmfdistdir}/doc/latex/parnotes/README.TEXLIVE

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 758996
- texlive-parnotes
- texlive-parnotes

