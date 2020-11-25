
all = importfile(".\all.xlsx", "Sheet1", [2, 9]);
mec = importfile(".\mec.xlsx", "Sheet1", [2, 9]);
local = importfile(".\local.xlsx", "Sheet1", [2, 9]);
all_6MHZ = importfile(".\all_6MHZ.xlsx", "Sheet1", [2, 9]);
all_8MHZ = importfile(".\all_8MHZ.xlsx", "Sheet1", [2, 9]);
all_12MHZ = importfile(".\all_12MHZ.xlsx", "Sheet1", [2, 9]);
%%
%figure
%subplot(1,2,1)
Step = [10:5:45];
plot(Step,all,'-o')
hold on
plot(Step,mec,'-*')
hold on
plot(Step,local,'-^')
hold on
plot(Step,all_6MHZ,'-+')
hold on
plot(Step,all_8MHZ,'-h')
hold on
plot(Step,all_12MHZ,'-d')
hold on
axis( [10 45 -1 15] )
xlabel('The number of UE')
ylabel('Sum of cost')
legend('all selection','only MEC selection','only local selection','all selection of 6MHZ','all selection of 8MHZ','all selection of 12MHZ')
%figure


