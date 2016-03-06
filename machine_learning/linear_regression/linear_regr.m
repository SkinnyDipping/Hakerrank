[nr_feat, count, err]=fscanf(stdin, '%f', 1);
[nr_probes, count, err]=fscanf(stdin, '%f', 1);
[data_mat, count, err]=fscanf(stdin, '%f', (nr_feat+1)*nr_probes);
[nr_quest, count, err]=fscanf(stdin, '%f',1);
[mat_quest,count,err]=fscanf(stdin,'%f',nr_quest*nr_feat);
data_mat=reshape(data_mat,(nr_feat+1),nr_probes)';
mat_quest=reshape(mat_quest,nr_feat,nr_quest)';
%data_mat
%mat_quest

X=[repmat(1,nr_probes,1) data_mat(:,1:nr_feat)];
y=[data_mat(:,nr_feat+1)];
Q=[repmat(1,nr_quest,1) mat_quest];

theta=inv(X'*X)*X'*y;
output=(theta'*Q')';
fprintf("%f\n",output);
