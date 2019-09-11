int necklace(int n, int *c, void reverse_interval(int name_first_bead, int name_last_bead)) {
  int num_breakpoints = (c[n-1] != c[0]) ? 1 : 0;
  for(int i = 1; i<n;i++)
    if(c[i] != c[i-1]) num_breakpoints++;
  int min_num_mosse = (num_breakpoints -2)/2;

  // TODO: fare le mosse

  
  return min_num_mosse;
}
