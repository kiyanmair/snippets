import quopri

def build_address_header(name, address):
    # QP encode the name.
    name = quopri.encodestring(name.encode('utf-8')).decode('ascii')
    name = f'=?utf-8?q?{name}?='
    # Divide the address into its local and domain parts.
    local, domain = address.split('@')
    # QP encode the local part.
    local = quopri.encodestring(local.encode('utf-8')).decode('ascii')
    local = f'=?utf-8?q?{local}?='
    # IDNA encode the domain part.
    domain = domain.encode('idna').decode('ascii')
    # Build the address header using the encoded parts.
    header = f'{name} <{local}@{domain}>'
    return header
