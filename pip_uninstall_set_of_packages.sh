pip list | grep jupyter | cut -d" " -f1 | xargs pip uninstall -y
