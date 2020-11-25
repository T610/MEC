
% 图3
length = 9;
all = importfile(".\all.xlsx", "Sheet1", [2,length]);
mec = importfile(".\mec.xlsx", "Sheet1", [2, length]);
local = importfile(".\local.xlsx", "Sheet1", [2,length]);
all_15_UEs = importfile(".\all_15_UEs.xlsx", "Sheet1", [2,length]);
all_20_UEs = importfile(".\all_20_UEs.xlsx", "Sheet1", [2, length]);
all_25_UEs = importfile(".\all_25_UEs.xlsx", "Sheet1", [2, length]);

%%

Step = [0.2:0.2:1.6];
plot(Step,all,'-o')
hold on
plot(Step,mec,'-*')
hold on
plot(Step,local,'-^')
hold on
plot(Step,all_15_UEs,'-+')
hold on
plot(Step,all_20_UEs,'-h')
hold on
plot(Step,all_25_UEs,'-d')
hold on
%axis( [10 45 -1 15] )

xlabel('The bandwidth of channel (HZ)')
ylabel('Sum of cost  (J)')
legend('all selection','only MEC selection','only loacl selection','all selection of 15 UEs','all selection of 20 UEs','all selection of 25 UEs')
%legend('wolf phc ','offloading only','wolf-phc-dl2-dh5','wolf-phc-dl1-dh4')
%figure
