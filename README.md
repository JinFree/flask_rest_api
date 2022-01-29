# flask_rest_api

prepare on osx

mysql
brew install mysql
brew install mysql-client
echo 'export PATH="/opt/homebrew/opt/mysql-client/bin:$PATH"' >> ~/.zshrc
export PKG_CONFIG_PATH="/opt/homebrew/opt/mysql-client/lib/pkgconfig"\n
export LDFLAGS="-L/opt/homebrew/opt/mysql-client/lib"\n  export CPPFLAGS="-I/opt/homebrew/opt/mysql-client/include"\n
brew install --cask mysqlworkbench