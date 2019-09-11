#define MAXN 1000

void swap(int *a, int *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

int necklace(int n, int *c, void reverse_interval(int name_first_bead, int name_last_bead)) {
  int name_of_bead_in_pos[MAXN];
  for(int i = 0; i < n; i++)
    name_of_bead_in_pos[i] = i+1;
  int num_mosse_fatte = 0;
  while(1) {
    int pos_change = 1;
    while( (pos_change < n) && (c[pos_change] == c[0]) )  pos_change++;
    int pos_back = pos_change + 1;
    while( (pos_back < n) && (c[pos_back] != c[0]) )  pos_back++;
    if ( (c[pos_change] == c[0]) || (pos_back >= n) || (c[pos_back] != c[0]) )  return num_mosse_fatte;
    reverse_interval(name_of_bead_in_pos[pos_back-1], name_of_bead_in_pos[pos_back]);
    num_mosse_fatte++;
    swap(&c[pos_back],&c[pos_back-1]);
    swap(&name_of_bead_in_pos[pos_back],&name_of_bead_in_pos[pos_back-1]);
  }
}
