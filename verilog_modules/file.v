// Task 2
module mult4x4(input clk, input [3:0] a, input [3:0] b, output [7:0] res);
  reg [3:0] rp1;
  reg [5:0] rp2;
  reg [6:0] rp3;
  reg [7:0] rp4;
  
  reg [4:0] aux1, aux2, aux3;
  
  always@(posedge clk)
    begin
      rp1 <= a & {4{b[0]}};
      aux1 <= rp1[3:1] + (a & {4{b[1]}});
      rp2 <= {aux1, rp1[0]};
      aux2 <= rp2[5:2] + (a & {4{b[2]}});
      rp3 <= {aux2, rp2[1:0]};
      aux3 <= rp3[6:3] + (a & {4{b[3]}});
      rp4 <= {aux3, rp3[2:0]};
    end
                                            
  assign res = rp4;
endmodule
                                            

// Task 4
module mult8x8(input clk, input [7:0] a, input [7:0] b, output [15:0] res);
  wire [7:0] res1, res2, res3, res4;
  mult4x4 mult4x4_1(clk, a[3:0], b[3:0], res1);
  mult4x4 mult4x4_2(clk, a[7:4], b[3:0], res2);
  mult4x4 mult4x4_3(clk, a[3:0], b[7:4], res3);
  mult4x4 mult4x4_4(clk, a[7:4], b[7:4], res4);
  
  assign res = {res4, 8'b0} + {res3, 4'b0} + {res2, 4'b0} + res1; 
endmodule
                                            
// Task 5
module mult16x16(input clk, input [15:0] a, input [15:0] b, output [31:0] res);
  wire [15:0] res1, res2, res3, res4;
  mult8x8 mult8x8_1(clk, a[7:0], b[7:0], res1);
  mult8x8 mult8x8_2(clk, a[15:8], b[7:0], res2);
  mult8x8 mult8x8_3(clk, a[7:0], b[15:8], res3);
  mult8x8 mult8x8_4(clk, a[15:8], b[15:8], res4);
  
  assign res = {res4, 16'b0} + {res3, 8'b0} + {res2, 8'b0} + res1; 
endmodule                                            