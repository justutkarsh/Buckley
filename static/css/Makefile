SOURCES = site admin
LESS_COMPESSOR ?= `which lessc`
WATCHR ?= `which watchr`

build:
	@@if [ ! -f ${WATCHR}] \
	then \
		echo "lessc required. try sudo gem install less"; \
		exit -1 \
	fi

watch:
	@@if test ! -z ${WATCHR}; then \
		echo "Watching less files..."; \
		watchr -e "watch('less/(.*\.less|bootstrap\.*\.less)') { system 'make' }"; \
	else \
		echo "You must have the watchr installed in order to watch Bootstrap less files."; \
		echo "You can install it by running: gem install watchr"; \
	fi

build_old:
	@@if test ! -z ${LESS_COMPESSOR}; then \
		sed -e 's/@VERSION/'"v${VERSION}"'/' -e 's/@DATE/'"${DATE}"'/' <${BOOTSTRAP_LESS} >${BOOTSTRAP_LESS}.tmp; \
		lessc ${BOOTSTRAP_LESS}.tmp > ${BOOTSTRAP}; \
		lessc ${BOOTSTRAP_LESS}.tmp > ${BOOTSTRAP_MIN} --compress; \
		rm -f ${BOOTSTRAP_LESS}.tmp; \
		echo "Bootstrap successfully built! - `date`"; \
	else \
		echo "You must have the LESS compiler installed in order to build Bootstrap."; \
		echo "You can install it by running: npm install less -g"; \
	fi

watch_old:
	@@if test ! -z ${WATCHR}; then \
		echo "Watching less files..."; \
		watchr -e "watch('less/.*\.less') { system 'make' }"; \
	else \
		echo "You must have the watchr installed in order to watch Bootstrap less files."; \
		echo "You can install it by running: gem install watchr"; \
	fi

.PHONY: build watch