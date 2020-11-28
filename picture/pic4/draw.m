


alldldh = importfile(".\all_dl_dh.xlsx", "Sheet1", [8, 14])
dl =   [0.0005:0.0005:0.004]
dh = [0.004:0.002:0.016]
 bar3(alldldh,0.5)
 axis( [  0.75 8.25 0.75 7.25 80 110] )
%set(gca,'xtick',0:100:2500) 
%%

xlabel(' \delta_{l}')
ylabel('\delta_{h}')
zlabel('Reward')
%legend('local only','wolf phc ','mec only','wolf-phc-dl2-dh5','wolf-phc-dl1-dh4')
%legend('wolf phc ','offloading only','wolf-phc-dl2-dh5','wolf-phc-dl1-dh4')
%figure

0.0005,	0.001	,0.0015,	0.002,	0.0025	,0.003,	0.0035,	0.004

0.004	,0.006	,0.008	,0.01,	0.012	,0.014	,0.016

