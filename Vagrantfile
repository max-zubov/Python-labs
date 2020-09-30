Vagrant.configure("2") do |config|

  config.vm.define "vm-1657" do |nodeconfig|
    nodeconfig.vm.box = "bento/centos-8.2"
#   config.vm.box_version = "202007.17.0"
    nodeconfig.vm.hostname = "vm-1657"
    nodeconfig.ssh.insert_key = false
    nodeconfig.vm.provider :virtualbox do |vb|
                vb.name = "vm-1657"
                vb.cpus = "2"
                vb.memory = "2048"
                vb.gui = false
    end
    nodeconfig.vm.provision "shell", inline: <<-'SCRIPT'
#      dnf -y update
      dnf -y install @development zlib-devel bzip2 bzip2-devel readline-devel \
         sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils
#      su - vagrant -c 'curl https://pyenv.run | bash'
      su - vagrant -c 'curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash'
      echo 'PATH="$HOME/.pyenv/bin:$PATH"' >> /home/vagrant/.bashrc
      echo 'export PATH' >> /home/vagrant/.bashrc
#      su - vagrant -c 'eval "$(pyenv init -)"'
#      su - vagrant -c 'eval "$(pyenv virtualenv-init -)"'
      echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile
      echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bash_profile
      su - vagrant -c 'pyenv install 2.7.18 && pyenv virtualenv 2.7.18 dev-2718'
      su - vagrant -c 'pyenv install 3.5.10 && pyenv virtualenv 3.5.10 dev-3510'
#      su - vagrant -c 'pyenv install 3.8.5 && pyenv virtualenv 3.8.5 dev-385'
    SCRIPT
  end
end
