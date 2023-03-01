как создать ssh ключ: ssh-keygen -t ed25519 -C "your_email@example.com"

Запустите в терминале shh-agent: eval "$(ssh-agent -s)"

Добавьте свой приватный ключ SSH в ssh-agent: ssh-add ~/.ssh/id_ed25519

как склонировать репозиторий: git clone <url>




