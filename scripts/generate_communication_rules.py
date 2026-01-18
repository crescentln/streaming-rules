import os

def collect_domains(directory: str) -> set:
    domains = set()
    if not os.path.isdir(directory):
        return domains
    for fname in os.listdir(directory):
        if fname.endswith('.txt'):
            path = os.path.join(directory, fname)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    for line in f:
                        domain = line.strip()
                        if domain and not domain.startswith('#'):
                            domains.add(domain)
            except Exception:
                continue
    return domains

def main():
    platforms_dir = 'platforms_communication'
    output_dir = 'rules'
    os.makedirs(output_dir, exist_ok=True)
    domains = collect_domains(platforms_dir)
    # write conf and txt files
    conf_path = os.path.join(output_dir, 'communication_rulesets.conf')
    txt_path = os.path.join(output_dir, 'communication_rulesets.txt')
    with open(conf_path, 'w', encoding='utf-8') as cf, open(txt_path, 'w', encoding='utf-8') as tf:
        for domain in sorted(domains):
            cf.write(f'DOMAIN-SUFFIX,{domain}\n')
            tf.write(f'{domain}\n')

if __name__ == '__main__':
    main()
