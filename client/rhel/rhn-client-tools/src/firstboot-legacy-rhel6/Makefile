# Makefile for installing man pages for the up2date client
#

TOPMODULE	= rhn_register
MODULES		= rhn_login_gui \
		  rhn_start_gui rhn_choose_server_gui \
		  rhn_provide_certificate_gui rhn_create_profile_gui \
		  rhn_review_gui rhn_finish_gui rhn_choose_channel
TOPPYFILE	= $(addsuffix .py, $(TOPMODULE))
PYFILES		= $(addsuffix .py, $(MODULES))
TOPOBJECT	= $(TOPPYFILE)
OBJECTS		= $(PYFILES)

# Install stuff
INSTALL         = /usr/bin/install -c
INSTALL_DATA     = $(INSTALL) -m 644
INSTALL_DIR     = $(INSTALL) -m 755 --verbose -d

# Install Directories
SYSTEMFIRSTBOOTDIR	= $(PREFIX)/usr/share/firstboot/modules/
FIRSTBOOTDIR	= $(PREFIX)$(PYTHONPATH)/up2date_client/firstboot/


PYCHECKER       = /usr/bin/pychecker

all:: $(TOPOBJECT) $(OBJECTS)

install: all $(FIRSTBOOTDIR) $(SYSTEMFIRSTBOOTDIR)
	$(INSTALL_DATA) $(OBJECTS) $(FIRSTBOOTDIR)/
	$(INSTALL_DATA) $(TOPOBJECT) $(SYSTEMFIRSTBOOTDIR)/

$(SYSTEMFIRSTBOOTDIR) $(FIRSTBOOTDIR) : 
	@$(INSTALL_DIR) $@

clean:
	@rm -rf *.pyc *~ .*~ *.o

pychecker::
	@$(PYCHECKER) $(PYFILES) $(TOPPYFILE) || exit 0

