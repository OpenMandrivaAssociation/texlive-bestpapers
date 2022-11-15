Name:		texlive-bestpapers
Version:	38708
Release:	1
Summary:	A BibTeX package to produce lists of authors' best papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bestpapers
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bestpapers.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bestpapers.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Many people preparing their resumes find the requirement
"please list five (or six, or ten) papers authored by you". The
same requirement is often stated for reports prepared by
professional teams. The creation of such lists may be a
cumbersome task. Even more difficult is it to support such
lists over the time, when new papers are added. The BibTeX
style bestpapers.bst is intended to facilitate this task. It is
based on the idea that it is easier to score than to sort: We
can assign a score to a paper and then let the computer select
the papers with highest scores. This work was commissioned by
the Consumer Financial Protection Bureau, United States
Treasury. This package is in the public domain.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/bestpapers
%doc %{_texmfdistdir}/doc/bibtex/bestpapers

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
