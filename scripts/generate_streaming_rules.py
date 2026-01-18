import os


def main():
    platforms_dir = 'platforms'
    rules_dir = 'rules'
    os.makedirs(rules_dir, exist_ok=True)
    domains = []
    if os.path.isdir(platforms_dir):
        for filename in os.listdir(platforms_dir):
            filepath = os.path.join(platforms_dir, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            domains.append(line)
    unique_domains = sorted(set(domains))
    # write output files
    with open(os.path.join(rules_dir, 'streaming_rulesets.conf'), 'w', encoding='utf-8') as out:
        for d in unique_domains:
            out.write(f"{d}\n")
    with open(os.path.join(rules_dir, 'streaming_rulesets.txt'), 'w', encoding='utf-8') as out:
        for d in unique_domains:
            out.write(f"{d}\n")


if __name__ == '__main__':
    main()
