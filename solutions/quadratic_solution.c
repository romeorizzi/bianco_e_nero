#define BLACK 0
#define WHITE 1

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
  int primi_bianchi_pos[MAXN], num_primi_bianchi;
  while(1) {
    num_primi_bianchi = 0;
    if( (c[0] == WHITE) && (c[n-1] == BLACK))
      primi_bianchi_pos[num_primi_bianchi++] = 0;
    for(int i = 1; i < n; i++)
      if( (c[i] == WHITE) && (c[i-1] == BLACK))
	primi_bianchi_pos[num_primi_bianchi++] = i;
    if(num_primi_bianchi <= 1)
      return num_mosse_fatte;
    reverse_interval(name_of_bead_in_pos[primi_bianchi_pos[0]], name_of_bead_in_pos[primi_bianchi_pos[1]-1]);
    num_mosse_fatte++;
    int reverse_performed_in_local = 0;
    int i = primi_bianchi_pos[0], j = primi_bianchi_pos[1]-1; 
    while(! reverse_performed_in_local) {
      swap(&c[i],&c[j]);
      swap(&name_of_bead_in_pos[i],&name_of_bead_in_pos[j]);
      i = (i+1)%n;
      if(i==j) reverse_performed_in_local = 1;
      j = (j-1+n)%n;
      if(i==j) reverse_performed_in_local = 1;
    }
  }
}
