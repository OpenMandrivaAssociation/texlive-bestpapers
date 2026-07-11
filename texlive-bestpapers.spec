%global tl_name bestpapers
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A BibTeX package to produce lists of authors best papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/bestpapers
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bestpapers.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bestpapers.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Many people preparing their resumes find the requirement "please list
five (or six, or ten) papers authored by you". The same requirement is
often stated for reports prepared by professional teams. The creation of
such lists may be a cumbersome task. Even more difficult is it to
support such lists over the time, when new papers are added. The BibTeX
style bestpapers.bst is intended to facilitate this task. It is based on
the idea that it is easier to score than to sort: We can assign a score
to a paper and then let the computer select the papers with highest
scores. This work was commissioned by the Consumer Financial Protection
Bureau, United States Treasury. This package is in the public domain.

