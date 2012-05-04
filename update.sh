#!/bin/sh
ln -sFf $HOME/.linux_config/bin  $HOME/bin
ln -sf $HOME/.linux_config/.gitignore $HOME/.gitignore_global
ln -sf $HOME/.linux_config/.bash_profile  $HOME/.bash_profile
ln -sf $HOME/.linux_config/.gitconfig $HOME/.gitconfig
ln -sf $HOME/.linux_config/.vimrc.bundles.local   $HOME/.vimrc.bundles.local
ln -sf $HOME/.linux_config/.vimrc.local    $HOME/.vimrc.local

ln -sFf $HOME/.linux_config/astyle  $HOME/.vim/astyle
ln -sFf $HOME/.linux_config/myultisnips $HOME/.vim/myultisnips


