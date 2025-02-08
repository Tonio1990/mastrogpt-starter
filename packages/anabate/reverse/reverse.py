def reverse(args):
  inp = args.get("input",'')
  out = 'This provider reverse a string!'
  if inp != '':
    out = inp[::-1]
  return { "output": out}
